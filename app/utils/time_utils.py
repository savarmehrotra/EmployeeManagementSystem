from datetime import datetime, timedelta

SERVER_TIMEZONE_OFFSET = 2


def transform_to_local_time(utc_time: datetime) -> datetime:
    """
    Transforms UTC time to local time based on the mocked server timezone.

    Args:
        utc_time (datetime): The UTC time to be transformed.

    Returns:
        datetime: The local time.
    """
    return utc_time + timedelta(hours=SERVER_TIMEZONE_OFFSET)
