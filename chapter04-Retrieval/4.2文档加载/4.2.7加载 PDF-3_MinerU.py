import os
import requests
import dotenv
dotenv.load_dotenv()

def upload_files(file_paths: list[str]) -> str:
  """批量上传文件"""
  url = "https://mineru.net/api/v4/file-urls/batch"
  api_key = os.getenv("MINERU_API_KEY")
  header = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}",
  }

  files_info = [
    {
      "name": os.path.basename(file_path), # 文件名
      "is_ocr": True, # 是否启用 ocr
      "data_id": f"file_{i}", # 文件对应唯一标识 id
    }
    for i, file_path in enumerate(file_paths)
  ] # 动态生成文件信息

  data = {
    "enable_formula": True, # 是否开启公式识别
    "enable_table": True, # 是否开启表格识别
    "language": "ch", # 文档语言
    "files": files_info,
  }

  try:
    response = requests.post(url, headers=header, json=data)
    if response.status_code == 200:
      result = response.json()
      print("response success. result:{}".format(result))
      if result["code"] == 0:
        batch_id = result["data"]["batch_id"]
        urls = result["data"]["file_urls"]
        print("batch_id:{}\nurls:{}".format(batch_id, urls))
        for i in range(0, len(urls)):
          with open(file_paths[i], "rb") as f:
            res_upload = requests.put(urls[i], data=f)
            if res_upload.status_code == 200:
              print(f"{urls[i]} upload success")
            else:
              print(f"{urls[i]} upload failed")
        return batch_id
      else:
        print("apply upload url failed,reason:{}".format(result.msg))
    else:
      print(
        "response not success. status:{} ,result:{}".format(
          response.status_code, response
        )
      )
  except Exception as err:
    print(err)

def download_files(batch_id):
  """批量获取任务结果"""
  os.makedirs("parsed_files", exist_ok=True)
  url = f"https://mineru.net/api/v4/extract-results/batch/{batch_id}"
  api_key = os.getenv("MINERU_API_KEY")
  header = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}",
  }
  res = requests.get(url, headers=header)
  if res.status_code != 200:
    print(f"获取结果失败。状态码: {res.status_code}，响应: {res.text}")
    print("请检查:")
    print("1. MINERU_API_KEY 环境变量是否已设置")
    print("2. API Key 是否有效")
    print("3. batch_id 是否正确")
    return
  
  result = res.json()
  if not result or "data" not in result:
    print(f"响应格式错误: {result}")
    return
  
  extract_results = result["data"]["extract_result"]
  failed_files = set() # 失败文件集合
  done_files = set() # 完成文件集合
  while True:
    for result in extract_results:
      if result["state"] == "failed":
        failed_files.add(str(result))
      elif result["state"] == "done":
        done_files.add(str(result))
        full_zip_url = result["full_zip_url"]
        res_download = requests.get(full_zip_url, stream=True)
        with open(
          f"parsed_files/{result['file_name']}_{result['data_id']}.zip", "wb"
        ) as f:
          for chunk in res_download.iter_content(chunk_size=1024):
            f.write(chunk)
    if len(failed_files) + len(done_files) == len(extract_results):
      break
  for i in failed_files:
    print(i)
  for i in done_files:
    print(i)

file_paths = [r"assets\尚硅谷大模型项目实战之智选新闻1.0.pdf"]
batch_id = upload_files(file_paths)
download_files(batch_id)