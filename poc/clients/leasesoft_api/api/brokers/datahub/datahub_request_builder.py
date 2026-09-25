from __future__ import annotations
from collections.abc import Callable
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .item.with_data_hub_item_request_builder import WithDataHubItemRequestBuilder

class DatahubRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/Brokers/datahub
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new DatahubRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/Brokers/datahub", path_parameters)
    
    def by_data_hub_id(self,data_hub_id: str) -> WithDataHubItemRequestBuilder:
        """
        Gets an item from the clients.leasesoft_api.api.Brokers.datahub.item collection
        param data_hub_id: Unique identifier of the item
        Returns: WithDataHubItemRequestBuilder
        """
        if data_hub_id is None:
            raise TypeError("data_hub_id cannot be null.")
        from .item.with_data_hub_item_request_builder import WithDataHubItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["dataHubId"] = data_hub_id
        return WithDataHubItemRequestBuilder(self.request_adapter, url_tpl_params)
    

