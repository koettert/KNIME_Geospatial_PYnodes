#This defines the Geospatial KNIME category that is displayed in the node repository
import knime_extension as knext

category = knext.category(
    path="/",
    level_id="geo",
    name="Geospatial",
    description="Geospatial processing nodes",
    icon="icon.png",
)