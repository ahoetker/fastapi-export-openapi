import typer
import yaml


import json
import logging
import subprocess
from enum import Enum
from pathlib import Path
from typing import Any, Dict, List


class OutputTypeEnum(str, Enum):
    json = "JSON"
    yaml = "YAML"
    both = "BOTH"


def install_apt_packages(dependencies: List[str]) -> None:
    logging.info("Updating apt repository index")
    subprocess.check_call(["apt", "update"])
    logging.info("Installing apt dependencies")
    subprocess.check_call(["apt", "install", "-y", " ".join(dependencies)])


def write_json_openapi(openapi: Dict[str, Any], output_path: Path) -> None:
    logging.info(f"Writing OpenAPI to {str(output_path)}")
    with output_path.open("w") as f:
        json.dump(openapi, f, indent=2)


def write_yaml_openapi(openapi: Dict[str, Any], output_path: Path) -> None:
    logging.info(f"Writing OpenAPI to {str(output_path)}")
    with output_path.open("w") as f:
        yaml.dump(openapi, f)