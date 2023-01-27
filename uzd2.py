atzime = int(input("Ievadiet atzimi no 1 lidz 100 ==>"))


if atzime >= 0 and atzime <= 49:
    print("Atzime ir F limenis")

elif atzime >= 50 and atzime <= 59:
    print("Atzime ir E limenis")

elif atzime >= 60 and atzime <= 69:
    print("Atzime ir D limenis")

elif atzime >= 70 and atzime <= 79:
    print("Atzime ir C limenis")

elif atzime >= 80 and atzime <= 89:
    print("Atzime ir B limenis")

elif atzime >= 90 and atzime <= 100:
    print("Atzime ir A limenis")

else:
    print("Skaitlis ir mazaks par 0 vai lielaks par 100!")
