from typing import Dict, Union, Any
from xarray.core.dataset import DataVariables, Dataset
from xarray.core.coordinates import DatasetCoordinates


def get_variable_meta(
    variables_ds: Union[DataVariables, DatasetCoordinates]
) -> Dict[str, Any]:
    variables = {}
    for k, v in variables_ds.items():
        dtype = None
        if 'str' in v.dtype.name:
            dtype = 'string'
        if 'float' in v.dtype.name:
            dtype = 'float'
        if 'int' in v.dtype.name:
            dtype = 'float'
        variables[k] = {
            'data_type': dtype,
            'dimensions': v.dims,
            'attributes': v.attrs,
        }
    return variables


def get_group_meta(groupds: Dataset) -> Dict[str, Any]:
    group_dimensions = {k: v for k, v in groupds.dims.items()}
    group_attributes = groupds.attrs
    variables = get_variable_meta(groupds.data_vars)
    coordinates = get_variable_meta(groupds.coords)
    return {
        'dimensions': group_dimensions,
        'attributes': group_attributes,
        'variables': variables,
        'coordinates': coordinates,
    }
