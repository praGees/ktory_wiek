
# program pokazuje ktory to wiek

def century(year):
    print('Sprawdzam czy dodałą sie zmiana na githubie')
    if year<101:
        return 1
    wiek = year//100
    if year%100 != 0:
        wiek += 1
    return wiek


if __name__ == '__main__':
    print(century(211))