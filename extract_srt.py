import os
import re

def extract_subtitle_text(srt_file_path):
    """从srt文件中提取纯文本内容"""
    with open(srt_file_path, 'r', encoding='utf-8') as file:
        content = file.read()
        
    # 使用正则表达式移除序号和时间轴
    # 匹配模式：数字+换行+时间轴+换行+文本
    pattern = r'\d+\n\d{2}:\d{2}:\d{2},\d{3} --> \d{2}:\d{2}:\d{2},\d{3}\n'
    text_only = re.sub(pattern, '', content)
    
    # 清理多余的空行
    text_only = re.sub(r'\n{3,}', '\n\n', text_only)
    text_only = text_only.strip()
    
    return text_only

def process_srt_folder(folder_path):
    """处理文件夹中的所有srt文件"""
    # 确保文件夹路径存在
    if not os.path.exists(folder_path):
        print(f"错误：文件夹 '{folder_path}' 不存在")
        return
    
    # 遍历文件夹
    for filename in os.listdir(folder_path):
        if filename.endswith('.srt'):
            srt_path = os.path.join(folder_path, filename)
            output_filename = filename.replace('.srt', '_text.txt')
            output_path = os.path.join(folder_path, output_filename)
            
            try:
                # 提取文本
                text_content = extract_subtitle_text(srt_path)
                
                # 保存到新文件
                with open(output_path, 'w', encoding='utf-8') as file:
                    file.write(text_content)
                    
                print(f"成功处理：{filename} -> {output_filename}")
                
            except Exception as e:
                print(f"处理文件 {filename} 时出错：{str(e)}")

def main():
    # 获取用户输入的文件夹路径
    folder_path = input("请输入包含srt文件的文件夹路径：").strip()
    
    # 处理文件夹
    process_srt_folder(folder_path)
    print("处理完成！")

if __name__ == "__main__":
    main()
