from server import myCursor as cursor
from server import serverConnection as sConnection


class User:

    def searchTrainsByNo(self, trainInfo):
        exec = cursor.execute('SELECT * FROM trains WHERE train_name=%s OR train_number=%s', (trainInfo, trainInfo))
        return cursor.fetchone()