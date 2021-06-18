import typer

import importlib
import logging
from pathlib import Path
from typing import List, Optional

from fastapi_export_openapi.export_openapi import (
    OutputTypeEnum,
    install_apt_packages,
    write_json_openapi,
    write_yaml_openapi,
)

logging.basicConfig(format="%(asctime)s %(message)s", level=logging.INFO)

app = typer.Typer()


@app.command()
def export_openapi(
    fastapi_app_module: str,
    output_type: OutputTypeEnum = OutputTypeEnum.json,
    json_output_path: Path = Path("openapi.json"),
    yaml_output_path: Path = Path("openapi.yaml"),
    apt_package: Optional[List[str]] = typer.Option(None),
) -> None:
    """
    Write the application's OpenAPI schema to disk.
    """

    if len(apt_package) > 0:
        install_apt_packages(apt_package)

    app = importlib.import_module(fastapi_app_module).app
    openapi = app.openapi()

    if output_type == OutputTypeEnum.json:
        write_json_openapi(openapi, json_output_path)
    elif output_type == OutputTypeEnum.yaml:
        write_yaml_openapi(openapi, yaml_output_path)
    else:
        write_json_openapi(openapi, json_output_path)
        write_yaml_openapi(openapi, yaml_output_path)
