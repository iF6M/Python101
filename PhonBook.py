PhoneBook = {
    1111111111:'Amal',2222222222:'Mohammed',3333333333:'Khadijah',
    4444444444:'Abdullah',5555555555:'Rawan',6666666666:'Faisal',7777777777:'Layla'
}
Order = input('If you want to search Type S , if you want to add Type A ')
if Order =='S':
 OrderSearch = input('If you want to search by number write N , if you want to search by owner name write O ')
 if OrderSearch == 'N':
     OrderSearchByNumber = int (input('Type number phone '))
     if OrderSearchByNumber in PhoneBook.keys():
         print(PhoneBook[OrderSearchByNumber])
     elif len(str(OrderSearchByNumber))!=10  :
         print('This is invalid number')
     else:
         print('Sorry, the number is not found') 
 elif OrderSearch == 'O':
     OrderSearchByOwner = input('Type owner name ')
     for numbers,names in PhoneBook.items():
        if OrderSearchByOwner == names:
         print(numbers)
elif Order == 'A':
    OrderName = input('Enter phone owner name ')
    OrderNumber = int(input('Enter phone number '))
    PhoneBook[OrderNumber] = OrderName
    print('Number has been added name :',OrderName,' , number :',OrderNumber)
else:
    print('Try again')