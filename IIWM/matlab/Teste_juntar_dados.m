clear all

A=[1 5 10];
dados_A=[50 55 60];

B=[2 3 4 6 7 8 9];
dados_B=[10 15 18 20 22 24 26];

n_A=size(A)


dados_full=zeros(1,A(n_A(2)))


for kk=1:n_A(2)
dados_full(A(kk))=dados_A(kk);
end

n_B=size(B);

for nn=1:n_B(2)
dados_full(B(nn))=dados_B(nn);
end

dados_full

