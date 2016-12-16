def rotate(ciphered_password):
    new_ciphered_password = ['','','','']
    for i in range(4):
        for j in range(3, -1,-1):
            new_ciphered_password[i] += ciphered_password[j][i] 
    return new_ciphered_password

def recall_password(cipher_grille, ciphered_password):
    ans = ''
    for _ in range(4):
        for i,ii in enumerate(cipher_grille):
            for j,jj in enumerate(ii):
                if jj == 'X':
                    ans = ans + ciphered_password[i][j]
        cipher_grille = rotate(cipher_grille)       
    return ans
