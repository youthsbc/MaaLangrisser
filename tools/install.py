from pathlib import Path

import json
import shutil
import sys

from configure import configure_ocr_model


working_dir = Path(__file__).parent.parent.resolve()
install_path = working_dir / "install"
version = len(sys.argv) > 1 and sys.argv[1] or "v0.0.1"

if len(sys.argv) < 4:
    print("Usage: python install.py <version> <os> <arch>")
    print("Example: python install.py v1.0.0 win x86_64")
    sys.exit(1)

os_name = sys.argv[2]
arch = sys.argv[3]


def get_dotnet_platform_tag():
    if os_name == "win" and arch == "x86_64":
        return "win-x64"
    if os_name == "win" and arch == "aarch64":
        return "win-arm64"
    if os_name == "macos" and arch == "x86_64":
        return "osx-x64"
    if os_name == "macos" and arch == "aarch64":
        return "osx-arm64"
    if os_name == "linux" and arch == "x86_64":
        return "linux-x64"
    if os_name == "linux" and arch == "aarch64":
        return "linux-arm64"

    print("Unsupported OS or architecture.")
    print("available parameters:")
    print("version: e.g., v1.0.0")
    print("os: [win, macos, linux, android]")
    print("arch: [aarch64, x86_64]")
    sys.exit(1)


def install_deps():
    local_maafw_path = working_dir / "maafw"
    if local_maafw_path.exists():
        shutil.copytree(
            local_maafw_path,
            install_path / "maafw",
            dirs_exist_ok=True,
        )
        return

    if not (working_dir / "deps" / "bin").exists():
        print('Please download the MaaFramework to "deps" first.')
        sys.exit(1)

    if os_name == "android":
        shutil.copytree(
            working_dir / "deps" / "bin",
            install_path,
            dirs_exist_ok=True,
        )
        shutil.copytree(
            working_dir / "deps" / "share" / "MaaAgentBinary",
            install_path / "MaaAgentBinary",
            dirs_exist_ok=True,
        )
    else:
        shutil.copytree(
            working_dir / "deps" / "bin",
            install_path / "maafw",
            ignore=shutil.ignore_patterns(
                "*MaaDbgControlUnit*",
                "*MaaThriftControlUnit*",
                "*MaaRpc*",
                "*MaaHttp*",
                "*.node",
                "*MaaPiCli*",
            ),
            dirs_exist_ok=True,
        )
        maa_agent_binary_path = working_dir / "deps" / "share" / "MaaAgentBinary"
        if maa_agent_binary_path.exists():
            shutil.copytree(
                maa_agent_binary_path,
                install_path / "maafw" / "MaaAgentBinary",
                dirs_exist_ok=True,
            )


def install_resource():
    configure_ocr_model()

    shutil.copytree(
        working_dir / "assets" / "resource",
        install_path / "resource",
        dirs_exist_ok=True,
    )
    shutil.copy2(
        working_dir / "assets" / "interface.json",
        install_path,
    )

    interface_path = install_path / "interface.json"
    with open(interface_path, "r", encoding="utf-8") as f:
        interface = json.load(f)

    interface["version"] = version
    for resource in interface.get("resource", []):
        resource["path"] = ["./resource"]

    with open(interface_path, "w", encoding="utf-8") as f:
        json.dump(interface, f, ensure_ascii=False, indent=4)


def install_chores():
    shutil.copy2(
        working_dir / "README.md",
        install_path,
    )
    shutil.copy2(
        working_dir / "LICENSE",
        install_path,
    )

    for stale_mxu_name in ("mxu.exe", "mxu"):
        stale_mxu_path = install_path / stale_mxu_name
        if stale_mxu_path.exists():
            stale_mxu_path.unlink()

    mxu_exe_path = working_dir / "mxu.exe"
    if mxu_exe_path.exists():
        shutil.copy2(
            mxu_exe_path,
            install_path / "MaaLangrisser.exe",
        )

    mxu_path = working_dir / "mxu"
    if mxu_path.exists():
        shutil.copy2(
            mxu_path,
            install_path / "MaaLangrisser",
        )

    config_path = working_dir / "config"
    if config_path.exists():
        shutil.copytree(
            config_path,
            install_path / "config",
            dirs_exist_ok=True,
        )


def install_agent():
    agent_path = working_dir / "agent"
    if agent_path.exists():
        shutil.copytree(
            agent_path,
            install_path / "agent",
            dirs_exist_ok=True,
        )


if __name__ == "__main__":
    if install_path.exists():
        shutil.rmtree(install_path)
    install_path.mkdir(parents=True, exist_ok=True)

    install_deps()
    install_resource()
    install_chores()
    install_agent()

    print(f"Install to {install_path} successfully.")
