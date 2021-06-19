import typer

import importlib
import logging
from pathlib import Path
from typing import List

from fastapi_export_openapi.export_openapi import (
    OutputTypeEnum,
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
) -> None:
    """
    Write the application's OpenAPI schema to disk.
    """

    app = importlib.import_module(fastapi_app_module).app
    openapi = app.openapi()

    if output_type == OutputTypeEnum.json:
        write_json_openapi(openapi, json_output_path)
    elif output_type == OutputTypeEnum.yaml:
        write_yaml_openapi(openapi, yaml_output_path)
    else:
        write_json_openapi(openapi, json_output_path)
        write_yaml_openapi(openapi, yaml_output_path)
