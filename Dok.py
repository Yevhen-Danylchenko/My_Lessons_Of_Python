way = int(input("Задайте довжину шляху з пункта А до B\t"))
way1 = int(input("Задайте довжину шляху від пункта В до С\t"))
weight = int(input("Задайте вагу вантажу. \t"))

volume = 300

tmp = 0

if weight <= 500 and weight >= 1:
    way += way1
    way *= 1
    if way > volume:
        way -= volume
    else:
        if way > 300:
            print("Літак не долетить.\n")
        else:
            volume = 600
            way -= volume
            print(f"Літак треба дозаправити на { way} літрів.\n")
            print("Літак долетиь.\n")
            if weight <= 1000 and weight > 500:
                way += way1
                way *= 4
                volume = 300
                else: if way > volume:
                        way -= volume
                        else:
                            if way > 300:
                                print("Літак не долетить.\n")
                            else:
                                volume = 600
                                way -= volume
                                print(f"Літак треба дозаправити на { way} літрів.\n")
                                print("Літак долетиь.\n")
                                if weight <= 1500 and weight > 1000:
                                    way += way1
                                    way *= 7
                                    if way > volume:
                                        way -= volume
                                    else:
                                        if way > 300:
                                            print("Літак не долетить.\n")
                                        else:
                                            volume = 600
                                            way -= volume
                                            print(f"Літак треба дозаправити на {way} літрів.\n")
                                            print("Літак долетиь.\n")
                                            if weight <= 2000 and weight > 1500:
                                                way += way1
                                                way *= 9
                                                if way > volume:
                                                    way -= volume
                                                else:
                                                    if way > 300:
                                                        print("Літак не долетить.\n")
                                                    else:
                                                        volume = 600
                                                        way -= volume
                                                        print(f"Літак треба дозаправити на {way} літрів.\n")
                                                        print("Літак долетиь.\n")
else:
    volume = 600
    way -= volume
    print(f"Літак треба дозаправити на {way} літрів.\n")
    print("Літак долетить.\n")
