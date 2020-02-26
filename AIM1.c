#include<stdio.h>
#include<string.h>
#include<ctype.h>
#define MAX 100000
char plainText[MAX];
int cipherText[MAX];
int key;

void printCipher(int size){
	int i;
	puts("Cipher Text obtained is :");
	for(i=0;i<size;i++)
	{
		printf("%c",cipherText[i]);
	}
}

void getCipher(){
	int i;
	for(i=0;i<strlen(plainText);i++){
		if(islower(plainText[i])){
				
			cipherText[i]=((plainText[i]+key));
			if(cipherText[i]>'z'){
				cipherText[i]='a'+(cipherText[i]-'z')-1;
			}

				
		}
		else{
			cipherText[i]=((plainText[i]+key));	
		
			if(cipherText[i]>'Z'){
				cipherText[i]='A'+(cipherText[i]-'Z')-1;
			}

		}
	//printf("%d %d\t",plainText[i],cipherText[i]);
		
		
	}
	printCipher(i);


}



int main(){
	puts("Enter Plain Text : ");
	gets(plainText);
	puts("Enter key : ");
	scanf("%d",&key);
	getCipher();
	
	return 0;

}
