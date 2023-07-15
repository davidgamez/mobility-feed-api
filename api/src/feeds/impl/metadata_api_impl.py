#
#   MobilityData 2023
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
#

from feeds_gen.apis.metadata_api_base import BaseMetadataApi
from feeds_gen.models.metadata import Metadata


class MetadataApiImpl(BaseMetadataApi):
    """
    This class represents the implementation of the `/datasets` endpoints.
    All methods from the parent class `feeds_gen.apis.metadata_api_base.BaseMetadataApi` should be implemented.
    If a method is left blank the associated endpoint will return a 500 HTTP response.
    """
    def metadata_get(
        self,
    ) -> Metadata:
        """Get metadata about this API."""
        return Metadata(version="0.0.0")