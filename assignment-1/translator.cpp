#include <iostream>
#include <fstream>
#include <map>
#include <string>

using namespace std;

int main(){

	string data;
	ifstream input;
	input.open("32bit.asm");

	while(getline(input, data)){
		size_t endpos = data.find_last_not_of(" \t");
		if( string::npos != endpos ){
    		data = data.substr( 0, endpos+1 );
    	}
    	size_t startpos = data.find_first_not_of(" \t");
		if( string::npos != startpos ){
    		data = data.substr( startpos );
		}

		if(data.find("section") != string::npos)
			cout<<data<<endl;
		else if(data.find("extern printf") != string::npos)
			cout<<"global _start"<<endl;
		else if(data.find("global main")!= string::npos)
			cout<<endl;
		else if(data.find("message db")!= string::npos)
			cout<<data<<endl<<endl;
		else if(data.find("main:")!= string::npos)
			cout<<"_start:"<<endl;
		else if(data.compare("pushad")== 0){
			cout<<"mov		rax, 1"<<endl;
			cout<<"mov		rdi, 1"<<endl;
		}
		else if(data.find("push dword")!= string::npos)
			cout<<"mov		rsi, message"<<endl;
		else if(data.compare("call printf")== 0){
			cout<<"mov		rdx, 13"<<endl;
			cout<<"syscall"<<endl;
		}
		else if(data.compare("add esp, 4")== 0){
			cout<<"mov		rax, 60"<<endl;
			cout<<"mov		rdi, 0"<<endl;
		}
		else if(data.compare("popad")== 0){

		}
		else if(data.compare("ret")== 0){
			cout<<"syscall"<<endl;
		}
		


		
			




	}

	return 0;
}
