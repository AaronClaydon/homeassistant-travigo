"""Constants for travigo."""

from logging import Logger, getLogger

LOGGER: Logger = getLogger(__package__)

DOMAIN = "travigo"
ATTRIBUTION = "Data provided by http://jsonplaceholder.typicode.com/"

CONF_ORIGIN_STOP = "origin_stop"
CONF_DESTINATION_STOP = "destination_stop"
