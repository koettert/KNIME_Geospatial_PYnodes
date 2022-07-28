import logging
import knime_extension as knext
import pandas as pd
import geopandas as gp
import geo_category
import transformer_nodes

LOGGER = logging.getLogger(__name__)

        
@knext.node(name="Compute Length", node_type=knext.NodeType.MANIPULATOR, icon_path="icon.png", category=geo_category.category)
@knext.input_table(name="Geo table", description="Table with geometry column to compute the length for")
@knext.output_table(name="Geo table with area", description=" Geo input table with additional length column")
class ComputeLengthNode:
    """
    This node computes the area of a geo cell.
    """

    def configure(self, configure_context, input_schema_1):
        return input_schema_1.append(knext.Column(knext.double(), "length"))
 
    def execute(self, exec_context, input_1):
        gdf=gp.GeoDataFrame(input_1.to_pandas())
        gdf['length']=gdf.length
        #why do we need to convert the GeoDataFrame into a pandas data frame???
        return knext.Table.from_pandas(pd.DataFrame(gdf))
        