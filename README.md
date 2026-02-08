O objetivo desse projeto é aprender os conceitos fundamentais de multi-tenancy. Utilizei Docker, Nginx e Flask para identificar tenants por subdomínio e headers HTTP.

Quando o cliente digita um dominio no navegador:
`
cliente1.localhost
cliente2.localhost
`
* A requisição chega no Nginx, que encaminha para o app python.
* Informações como host e headers customizados são preservadas.
* A aplicação interpreta e retorna a saudação com o nome, cliente, e uma background color diferente para cada cliente.
Tudo isso rodando em containers Docker de forma isolada.