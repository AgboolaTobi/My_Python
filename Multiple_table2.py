# multiple = 1
# for multiple in range(1, 13):
#     for multiply in range(1, 21):
#         print(f"{multiply}\t * {multiple}\t = {multiply * multiple}\t", end="  ")
#     print()

# You can also use :< or :> or :^ to space effectively
multiple = 1
for multiple in range(1, 13):
    for multiply in range(1, 21):
        print(f"{multiply:>2} * {multiple:>3} = {multiply * multiple:^6}", end="  ")
    print()