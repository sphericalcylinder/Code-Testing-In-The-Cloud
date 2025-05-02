program variables
    implicit none
    
    integer :: amount
    real :: price
    character :: initial
    logical :: isAvailable

    ! Assign values to the variables
    amount = 10
    price = 19.99
    initial = 'A'
    isAvailable = .true.

    ! Print the values of the variables
    print *, "Amount: ", amount
    print *, "Price: ", price
    print *, "Initial: ", initial
    print *, "Is Available: ", isAvailable
    

end program variables