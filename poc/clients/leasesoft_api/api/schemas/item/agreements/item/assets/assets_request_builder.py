from __future__ import annotations
from collections.abc import Callable
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .item.with_asset_no_item_request_builder import WithAssetNoItemRequestBuilder

class AssetsRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/schemas/{tenantSchema}/agreements/{agreementNo}/assets
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new AssetsRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/schemas/{tenantSchema}/agreements/{agreementNo}/assets", path_parameters)
    
    def by_asset_no(self,asset_no: int) -> WithAssetNoItemRequestBuilder:
        """
        Gets an item from the clients.leasesoft_api.api.schemas.item.agreements.item.assets.item collection
        param asset_no: Unique identifier of the item
        Returns: WithAssetNoItemRequestBuilder
        """
        if asset_no is None:
            raise TypeError("asset_no cannot be null.")
        from .item.with_asset_no_item_request_builder import WithAssetNoItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["assetNo"] = asset_no
        return WithAssetNoItemRequestBuilder(self.request_adapter, url_tpl_params)
    

