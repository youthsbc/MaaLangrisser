<!-- markdownlint-disable MD033 MD041 -->
<p align="center">
  <img
    alt="MAA logo"
    src="./docs/images/almeda.png"
    width="180"
  />
</p>

<div align="center">

# MaaLangrisser

An automation assistant for Langrisser Mobile, powered by MaaFramework.

[![license](https://img.shields.io/github/license/youthsbc/MaaLangrisser?style=flat-square)](./LICENSE)
[![check](https://img.shields.io/github/actions/workflow/status/youthsbc/MaaLangrisser/check.yml?branch=main&label=check&style=flat-square)](https://github.com/youthsbc/MaaLangrisser/actions/workflows/check.yml)
[![build](https://img.shields.io/github/actions/workflow/status/youthsbc/MaaLangrisser/install.yml?branch=main&label=build&style=flat-square)](https://github.com/youthsbc/MaaLangrisser/actions/workflows/install.yml)
[![release](https://img.shields.io/github/v/release/youthsbc/MaaLangrisser?style=flat-square)](https://github.com/youthsbc/MaaLangrisser/releases)
[![stars](https://img.shields.io/github/stars/youthsbc/MaaLangrisser?style=flat-square)](https://github.com/youthsbc/MaaLangrisser/stargazers)

</div>

## Introduction

MaaLangrisser is a MaaFramework project for automating routine Langrisser
Mobile tasks on Android emulators. It uses image recognition and simulated
control to handle repeatable daily actions, so you can spend less time tapping
through menus.

The current resource set targets the Global Server English client.

> This project is community-maintained and is not affiliated with the official
> Langrisser Mobile team.

## Download

Download the latest package from [GitHub Releases](https://github.com/youthsbc/MaaLangrisser/releases).

Release artifacts are built for:

- Windows x86_64 / aarch64
- macOS x86_64 / aarch64
- Linux x86_64

## Quick Start

1. Install and start an Android emulator, then launch Langrisser Mobile.
2. Extract the MaaLangrisser release package.
3. Run `MaaLangrisser.exe` on Windows, `MaaLangrisser.app` on macOS, or `MaaLangrisser` on Linux.
4. Select the `Android emulator` controller and the `Global Server - English` resource.
5. Choose the tasks you want to run, then start execution.

If MaaLangrisser cannot find your emulator, check that ADB is enabled in the
emulator settings and that the game screen is visible before starting tasks.

## Features

Currently available tasks include:

- Start the game and enter the world map.
- Collect Floating Realm resources.
- Sweep Bonds shards for the top 3 characters.
- Sweep Time Rift elite stages.
- Run daily Arena battles.
- Use Friendship Summon vouchers.
- Claim mail, friend points, daily mission rewards, and weekly Relics of the Gods.
- Clear selected world events.
- Sweep Secret Realm daily content, Ways of the Laws, Eternal Temple, Stolen Treasure, and Timeless Trial.
- Run Ways of the Laws manually with stage selection.
- Stop the app after automation finishes.

Some tasks provide options in the MaaFramework-compatible UI, such as Time Rift
stage, Aniki Gym stage, and Ways of the Laws stage.

## Development

This project follows the standard MaaFramework project layout:

- `assets/interface.json`: project interface and UI task definitions.
- `assets/resource/pipeline`: automation pipelines.
- `assets/resource/image`: recognition templates.
- `tools/install.py`: packaging script used by CI releases.

Useful local commands:

```powershell
git submodule update --init --recursive
npm ci
npx @nekosu/maa-tools check
python tools/configure.py
python tools/install.py v0.0.1-local win x86_64
```

For MaaFramework concepts and project interface details, see the [MaaFramework documentation](https://maafw.com/).

## Community

Bug reports, task requests, and recognition template improvements are welcome
through [Issues](https://github.com/youthsbc/MaaLangrisser/issues) and
[Pull Requests](https://github.com/youthsbc/MaaLangrisser/pulls).

When reporting recognition problems, please include your operating system,
emulator name, emulator resolution/DPI, the affected task, and an unobstructed
screenshot from the emulator or ADB.

## Acknowledgements

MaaLangrisser is built with [MaaFramework](https://github.com/MaaXYZ/MaaFramework) and the generic MaaFramework UI tooling.

Thanks to the Maa community and all contributors who make project templates,
tools, documentation, and common assets available.

Thanks to the following developers for contributing to this project:

[![Contributors](https://contrib.rocks/image?repo=youthsbc/MaaLangrisser&max=1000)](https://github.com/youthsbc/MaaLangrisser/graphs/contributors)
