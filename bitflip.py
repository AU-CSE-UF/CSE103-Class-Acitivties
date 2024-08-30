bit_str = input("Enter a binary number : ")

bin_bit_str = int(bit_str, 2)
bin_msk = 2**(len(bit_str) + 1) - 1

flp_bin_bit = bin_bit_str ^ bin_msk

flp_bit_str = bin(flp_bin_bit)[3:]
print(flp_bit_str)