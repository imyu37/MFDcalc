import FreeSimpleGUI as sg
import math


def calculate_mfd():
    # 设置主题
    sg.theme("LightBlue2")

    # 布局设计
    layout = [
        [
            sg.Text("波长 (nm):", font=("Microsoft YaHei",)),
            sg.InputText(
                key="wavelength", size=(10, 1), font=("Arial",), default_text="488"
            ),
        ],
        [
            sg.Text("数值孔径 (NA):", font=("Microsoft YaHei",)),
            sg.InputText(key="na", size=(10, 1), font=("Arial",), default_text="0.06"),
        ],
        [
            sg.Text("纤芯直径 (μm):", font=("Microsoft YaHei",)),
            sg.InputText(
                key="core_diameter", size=(10, 1), font=("Arial",), default_text="4.0"
            ),
        ],
        [sg.HorizontalSeparator()],
        [
            sg.Button("计算", key="calculate", font=("Microsoft YaHei",)),
            sg.Button("清除", key="clear", font=("Microsoft YaHei",)),
            sg.Button("退出", key="exit", font=("Microsoft YaHei",)),
        ],
        [
            sg.Text("计算结果:", font=("Microsoft YaHei", 12)),
            sg.Text("", key="result", size=(20, 1), font=("Arial", 12)),
        ],
    ]

    # 创建窗口
    window = sg.Window("模场直径计算器", layout)

    # 事件循环
    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED or event == "exit":
            break

        if event == "clear":
            window["wavelength"].update("")
            window["na"].update("")
            window["core_diameter"].update("")
            window["result"].update("")

        if event == "calculate":
            try:
                # 获取输入值
                wavelength = float(values["wavelength"])
                na = float(values["na"])
                core_diameter = float(values["core_diameter"])

                # 转换为米
                wavelength_m = wavelength * 1e-9
                core_radius_m = (core_diameter / 2) * 1e-6

                # 计算V数
                V = (2 * math.pi * core_radius_m * na) / wavelength_m

                # 计算模场直径 ( Dietrich Marcuse公式)
                mfd = (2 * core_radius_m) * (0.65 + 1.619 / (V**1.5) + 2.879 / (V**6))

                # 转换为微米
                mfd_um = mfd * 1e6

                # 显示结果
                window["result"].update(f"{mfd_um:.2f} μm")

            except ValueError:
                sg.popup_error("请输入有效的数值!")

    window.close()


if __name__ == "__main__":
    calculate_mfd()
