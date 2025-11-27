import os
import re


def replace_markdown_content(root_folder, old_content, new_content):
    """
    批量替换所有子文件夹中Markdown文件的内容

    参数:
    root_folder: 根文件夹路径
    old_content: 要替换的旧内容
    new_content: 替换后的新内容
    use_regex: 是否使用正则表达式匹配
    """

    # 检查根文件夹是否存在
    if not os.path.exists(root_folder):
        print(f"错误：文件夹 '{root_folder}' 不存在")
        return

    # 计数器
    total_files = 0
    replaced_files = 0

    # 遍历根文件夹下的所有子文件夹和文件
    for root, dirs, files in os.walk(root_folder):
        for file in files:
            # 只处理Markdown文件
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                total_files += 1

                try:
                    # 读取文件内容
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()

                    # 备份原始内容
                    original_content = content

                    # 执行替换

                    # 使用普通字符串替换
                    content = content.replace(old_content, new_content)

                    # 如果内容有变化，则写入文件
                    if content != original_content:
                        with open(file_path, 'w', encoding='utf-8') as f:
                            f.write(content)
                        print(f"✓ 已替换: {file_path}")
                        replaced_files += 1
                    else:
                        print(f"- 无变化: {file_path}")

                except Exception as e:
                    print(f"✗ 处理失败: {file_path} - 错误: {str(e)}")

    print(f"\n替换完成！")
    print(f"总共扫描: {total_files} 个Markdown文件")
    print(f"成功替换: {replaced_files} 个文件")

# 使用示例
if __name__ == "__main__":
    # 配置参数
    root_folder = 'D:\PycharmProjects\learn_pytorch\TUku\markdown_folder'



    old_content = input("请输入要替换的内容: ").strip()
    new_content = input("请输入替换后的内容: ").strip()


    # 确认操作
    confirm = input("\n确认执行替换操作吗？(y/n): ").strip().lower()
    if confirm == 'y':
        print("\n开始替换...")
        replace_markdown_content(root_folder, old_content, new_content)
    else:
        print("操作已取消")


















