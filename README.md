RMII & SMII interface
===========================
10M/100M 以太网 RMII 和 SMII 接口的 FPGA 实现

# 目的

一些以太网 PHY 芯片使用 RMII 或 SMII 接口，然而 FPGA 中的软核或硬核MAC往往是MII接口的。
为了实现这些 PHY 与 MAC 的适配，该库用 Verilog 实现了 MII 转 RMII 和 MII 转 SMII

# RMII interface

## 代码

**rmii_phy_if.v** 是 RMII 接口实现，即 MII 转 RMII。

## 示例

请解压 arty_rmii.zip ，得到 vivado 工程，请用 vivado2019.1 打开。

该工程修改自 [github.com/alexforencich/verilog-ethernet](https://github.com/alexforencich/verilog-ethernet)/example/Arty

为了进行该测试，你需要在 [Arty开发板](https://store.digilentinc.com/arty-a7-artix-7-fpga-development-board-for-makers-and-hobbyists/) 的 PMOD JA 和 JB 上外接 RMII-PHY （例如LAN8720）。

该工程会把 192.168.0.128:1234 上收到的 UDP 包回环，你可以把 FPGA 的以太网与 PC 机连在同一个局域网内（例如直连或通过交换机），然后使用 Python3 运行 udp_loopback.py。若回环测试报告正常，说明网络通信成功。

# SMII interface

## 代码

**smii_phy_if.v** 是 SMII 接口实现，即 MII 转 SMII。

## 示例

请解压 arty_smii.zip ，得到 vivado 工程，请用 vivado2019.1 打开。

该工程修改自 [github.com/alexforencich/verilog-ethernet](https://github.com/alexforencich/verilog-ethernet)/example/Arty

为了进行该测试，你需要在 [Arty开发板](https://store.digilentinc.com/arty-a7-artix-7-fpga-development-board-for-makers-and-hobbyists/) 的 PMOD JA 上外接 SMII-PHY （例如KSZ8041TLI-S）。

该工程会把 192.168.0.128:1234 上收到的 UDP 包回环，你可以把 FPGA 的以太网与 PC 机连在同一个局域网内（例如直连或通过交换机），然后使用 Python3 运行 udp_loopback.py。若回环测试报告正常，说明网络通信成功。

## 仿真

请解压 tb_smii.zip ，得到 vivado 工程，请用 vivado2019.1 打开。

该工程在 RX 通道上生成假的、短小的 SMII 包，通过 smii_phy_if.v 转换成 MII RX 的波形。同时，在 TX 通道上生成假的、短小的 MII 包，通过 smii_phy_if.v 转换成 SMII TX 的波形。

在vivado中点击 "run behavior simulation" 即可观察波形。

# 参考资料

* [github.com/alexforencich/verilog-ethernet](github.com/alexforencich/verilog-ethernet)

* RMII 接口标准：见 doc/RMII.pdf

* SMII 接口标准：见 doc/SMII.pdf
