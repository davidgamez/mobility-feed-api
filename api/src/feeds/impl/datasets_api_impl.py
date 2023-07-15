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

from datetime import date
from feeds_gen.apis.datasets_api_base import BaseDatasetsApi
from feeds_gen.models.bounding_box import BoundingBox
from feeds_gen.models.gtfs_dataset import GtfsDataset


class DatasetsApiImpl(BaseDatasetsApi):
    """
    This class represents the implementation of the `/datasets` endpoints.
    All methods from the parent class `feeds_gen.apis.datasets_api_base.BaseDatasetsApi` should be implemented.
    If a method is left blank the associated endpoint will return a 500 HTTP response.
    """

    def datasets_id_gtfs_get(
            self,
            id: str,
    ) -> GtfsDataset:
        """Get the specified dataset from the Mobility Database."""
        return GtfsDataset(id="datasetFoo", feed_id="feedFoo", hosted_url="http://www.abc.com", note="note",
                           download_date=date.today(), creation_date=date.today(), last_update_date=date.today(),
                           hash="123", locations=[], bounding_box=BoundingBox(), features=[])
