from twindb_backup.status.mysql_status import MySQLStatus


def test_backup_duration(deprecated_status_raw_content):
    status = MySQLStatus(deprecated_status_raw_content)
    copy = status["master1/hourly/mysql/mysql-2018-03-28_04_11_16.xbstream.gz"]
    assert copy.duration == 19
