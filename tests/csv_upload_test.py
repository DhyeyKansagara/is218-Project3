from os.path import exists

file_exists = exists("app/uploads/music.csv")

def test_checks_csv():
    """This checks if the csv file was uploaded"""
    assert file_exists == True


