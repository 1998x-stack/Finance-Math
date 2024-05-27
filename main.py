structure = {
    "第1章 引论：简单市场模型": [
        "1.1 基本概念和假设",
        "1.2 无套利原则",
        "1.3 单期二叉树模型",
        "1.4 风险和收益",
        "1.5 远期合约",
        "1.6 看涨期权和看跌期权",
        "1.7 用期权管理风险"
    ],
    "第2章 无风险资产": [
        {
            "2.1 货币的时间价值": [
                "2.1.1 单利",
                "2.1.2 按期复合",
                "2.1.3 支付流",
                "2.1.4 连续复合",
                "2.1.5 如何比较复合方法"
            ]
        },
        {
            "2.2 货币市场": [
                "2.2.1 零息债券",
                "2.2.2 附息债券",
                "2.2.3 货币市场账户"
            ]
        }
    ],
    "第3章 风险资产": [
        {
            "3.1 股票价格动态": [
                "3.1.1 收益",
                "3.1.2 期望收益"
            ]
        },
        {
            "3.2 二叉树模型": [
                "3.2.1 风险中性概率",
                "3.2.2 鞅性质"
            ]
        },
        {
            "3.3 其他模型": [
                "3.3.1 三叉树模型",
                "3.3.2 连续时间极限"
            ]
        }
    ],
    "第4章 离散时间市场模型": [
        {
            "4.1 股票和货币市场模型": [
                "4.1.1 投资策略",
                "4.1.2 无套利原则",
                "4.1.3 应用于二叉树模型",
                "4.1.4 资产定价基本定理"
            ]
        },
        "4.2 模型的扩展"
    ],
    "第5章 资产组合管理": [
        "5.1 风险",
        {
            "5.2 两证券": [
                "5.2.1 资产组合的期望收益和风险"
            ]
        },
        {
            "5.3 多个证券": [
                "5.3.1 资产组合的风险和期望收益",
                "5.3.2 有效边界"
            ]
        },
        {
            "5.4 资本资产定价模型": [
                "5.4.1 资本市场线",
                "5.4.2 贝塔因子",
                "5.4.3 证券市场线"
            ]
        }
    ],
    "第6章 远期合约和期货合约": [
        {
            "6.1 远期合约": [
                "6.1.1 远期价格",
                "6.1.2 远期合约的价值"
            ]
        },
        {
            "6.2 期货": [
                "6.2.1 定价",
                "6.2.2 利用期货套期保值"
            ]
        }
    ],
    "第7章 期权：一般性质": [
        "7.1 定义",
        "7.2 看跌期权一看涨期权平价",
        {
            "7.3 期权价格的边界": [
                "7.3.1 欧式期权",
                "7.3.2 不支付红利的股票的欧式看涨期权和美式看涨期权",
                "7.3.3 美式期权"
            ]
        },
        {
            "7.4 决定期权价格的变量": [
                "7.4.1 欧式期权",
                "7.4.2 美式期权"
            ]
        },
        "7.5 期权的时间价值"
    ],
    "第8章 期权定价": [
        {
            "8.1 二叉树模型中的欧式期权": [
                "8.1.1 单期",
                "8.1.2 两期模型",
                "8.1.3 一般的N期模型",
                "8.1.4 考克斯-罗斯-鲁宾斯坦公式"
            ]
        },
        "8.2 在二叉树模型中的美式期权",
        "8.3 布莱克-斯科尔斯公式"
    ],
    "第9章 金融工程": [
        {
            "9.1 期权头寸套期保值": [
                "9.1.1 德尔塔套期保值",
                "9.1.2 用希腊字母表示的参数",
                "9.1.3 应用"
            ]
        },
        {
            "9.2 经营风险套期保值": [
                "9.2.1 风险价值",
                "9.2.2 案例研究"
            ]
        },
        {
            "9.3 利用衍生产品投机": [
                "9.3.1 工具",
                "9.3.2 案例研究"
            ]
        }
    ],
    "第10章 可变利率": [
        {
            "10.1 与到期日无关的收益率": [
                "10.1.1 在单个债券上的投资",
                "10.1.2 久期",
                "10.1.3 债券资产组合",
                "10.1.4 动态套期保值"
            ]
        },
        {
            "10.2 一般的期限结构": [
                "10.2.1 远期利率",
                "10.2.2 货币市场账户"
            ]
        }
    ],
    "第11章 随机利率": [
        "11.1 二叉树模型",
        {
            "11.2 债券的套利定价": [
                "11.2.1 风险中性概率"
            ]
        },
        {
            "11.3 利率衍生证券": [
                "11.3.1 期权",
                "11.3.2 互换",
                "11.3.3 利率的上限和下限"
            ]
        }
    ]
}


import os
import json
from typing import Union, Dict, List, Any

def create_directories_and_files(
    base_path: str, 
    structure: Dict[str, Any], 
    readme_file, 
    parent_path: str = "", 
    level: int = 1
):
    """
    根据给定的目录结构创建目录和文件，并生成 README.md 文件。

    Args:
        base_path (str): 根目录路径。
        structure (Dict[str, Any]): 目录结构的嵌套字典。
        readme_file (File): 用于写入README内容的文件对象。
        parent_path (str): 父目录路径。
        level (int): 目录的层级，用于确定 README 标题级别。

    Returns:
        None
    """
    heading = "#" * level

    for key, value in structure.items():
        current_path = os.path.join(base_path, key.replace(" ", "_").replace("/", "_").replace("-", "_"))

        # 创建目录
        os.makedirs(current_path, exist_ok=True)

        # 在README中添加章节标题
        if parent_path:
            readme_file.write(f"{heading} {parent_path}/{key}\n\n")
        else:
            readme_file.write(f"{heading} {key}\n\n")

        # 递归调用创建子目录和文件
        if isinstance(value, dict) and value:
            create_directories_and_files(
                current_path, 
                value, 
                readme_file, 
                parent_path + "/" + key if parent_path else key, 
                level + 1
            )
        elif isinstance(value, list):
            for idx, item in enumerate(value):
                if isinstance(item, dict) and item:
                    create_directories_and_files(
                        current_path, 
                        item, 
                        readme_file, 
                        parent_path + "/" + key if parent_path else key, 
                        level + 1
                    )
                else:
                    item = f"{idx:02d}_{item}"
                    file_name = item.replace(" ", "_").replace("/", "_").replace("-", "_") + ".py"
                    file_path = os.path.join(current_path, file_name)
                    with open(file_path, 'w', encoding='utf-8') as file:
                        file.write(f"# {item}\n\n")
                        file.write(f'"""\nLecture: {parent_path}/{key}\nContent: {item}\n"""\n\n')

                    # 在README中添加文件链接
                    item_clean = item.replace(" ", "_").replace("/", "_").replace("-", "_")
                    parent_clean = parent_path.replace(" ", "_").replace("/", "_").replace("-", "_")
                    key_clean = key.replace(" ", "_").replace("/", "_").replace("-", "_")
                    readme_file.write(f"- [{item}](./{parent_clean}/{key_clean}/{item_clean}.py)\n")
        else:
            # 创建文件并写入初始内容
            file_name = key.replace(" ", "_").replace("/", "_").replace("-", "_") + ".py"
            file_path = os.path.join(current_path, file_name)
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(f"# {key}\n\n")
                file.write(f'"""\nLecture: {parent_path}/{key}\nContent: {key}\n"""\n\n')

            # 在README中添加文件链接
            parent_clean = parent_path.replace(" ", "_").replace("/", "_").replace("-", "_")
            key_clean = key.replace(" ", "_").replace("/", "_").replace("-", "_")
            readme_file.write(f"- [{key}](./{parent_clean}/{key_clean}/{file_name})\n")

        # 添加空行以分隔不同的章节
        readme_file.write("\n")

def main():
    root_dir = './'
    # 创建根目录
    os.makedirs(root_dir, exist_ok=True)

    # 创建 README.md 文件
    with open(os.path.join(root_dir, "README.md"), 'w', encoding='utf-8') as readme_file:
        readme_file.write("# 金融数学\n\n")
        readme_file.write("这是一个关于金融数学的目录结构。\n\n")
        create_directories_and_files(root_dir, structure, readme_file)

    print("目录和文件结构已生成，并创建 README.md 文件。")

if __name__ == "__main__":
    main()