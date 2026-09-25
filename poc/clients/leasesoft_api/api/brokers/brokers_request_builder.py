from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from kiota_abstractions.default_query_parameters import QueryParameters
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.request_adapter import RequestAdapter
from kiota_abstractions.request_information import RequestInformation
from kiota_abstractions.request_option import RequestOption
from kiota_abstractions.serialization import Parsable, ParsableFactory
from typing import Any, Optional, TYPE_CHECKING, Union
from warnings import warn

if TYPE_CHECKING:
    from ...models.ls_broker_details import LsBrokerDetails
    from .datahub.datahub_request_builder import DatahubRequestBuilder
    from .item.broker_golden_record_item_request_builder import BrokerGoldenRecordItemRequestBuilder
    from .short_name.short_name_request_builder import ShortNameRequestBuilder

class BrokersRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/Brokers
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new BrokersRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/Brokers{?dataHubId*,tenantSchema*}", path_parameters)
    
    def by_broker_golden_record_id(self,broker_golden_record_id: str) -> BrokerGoldenRecordItemRequestBuilder:
        """
        Gets an item from the clients.leasesoft_api.api.Brokers.item collection
        param broker_golden_record_id: Unique identifier of the item
        Returns: BrokerGoldenRecordItemRequestBuilder
        """
        if broker_golden_record_id is None:
            raise TypeError("broker_golden_record_id cannot be null.")
        from .item.broker_golden_record_item_request_builder import BrokerGoldenRecordItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["brokerGoldenRecord%2Did"] = broker_golden_record_id
        return BrokerGoldenRecordItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[BrokersRequestBuilderGetQueryParameters]] = None) -> Optional[LsBrokerDetails]:
        """
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[LsBrokerDetails]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ...models.ls_broker_details import LsBrokerDetails

        return await self.request_adapter.send_async(request_info, LsBrokerDetails, None)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[BrokersRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json, text/plain;q=0.9")
        return request_info
    
    def with_url(self,raw_url: str) -> BrokersRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: BrokersRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return BrokersRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def datahub(self) -> DatahubRequestBuilder:
        """
        The datahub property
        """
        from .datahub.datahub_request_builder import DatahubRequestBuilder

        return DatahubRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def short_name(self) -> ShortNameRequestBuilder:
        """
        The shortName property
        """
        from .short_name.short_name_request_builder import ShortNameRequestBuilder

        return ShortNameRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class BrokersRequestBuilderGetQueryParameters():
        def get_query_parameter(self,original_name: str) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            param original_name: The original query parameter name in the class.
            Returns: str
            """
            if original_name is None:
                raise TypeError("original_name cannot be null.")
            if original_name == "data_hub_id":
                return "dataHubId"
            if original_name == "tenant_schema":
                return "tenantSchema"
            return original_name
        
        data_hub_id: Optional[str] = None

        tenant_schema: Optional[str] = None

    
    @dataclass
    class BrokersRequestBuilderGetRequestConfiguration(RequestConfiguration[BrokersRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

