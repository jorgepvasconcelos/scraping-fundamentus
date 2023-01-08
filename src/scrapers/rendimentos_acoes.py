import httpx
from parsel import Selector


def scrape_rendimentos_acoes(codigos: list[str]):
    for codigo in codigos:
        url = f'https://www.fundamentus.com.br/proventos.php?papel={codigo}'
        response = httpx.post(url=url)

        selector = Selector(text=response.text)

        linhas = selector.css('tbody > tr')

        rendimentos = []
        for linha in linhas:
            rendimentos.append(
                {
                    "DATA COM": linha.css('td:nth-child(1)::text').get(),
                    "VALOR": linha.css('td:nth-child(2)::text').get(),
                    "TIPO": linha.css('td:nth-child(3)::text').get(),
                    "DATA PAGAMENTO": linha.css('td:nth-child(4)::text').get(),
                    "PELA QTD ACOES": linha.css('td:nth-child(5)::text').get(),
                }
            )
