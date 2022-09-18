import requests
from parsel import Selector


def get_acoes() -> list:
    headers = {
        'authority': 'fundamentus.com.br',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-language': 'en-US,en;q=0.9,pt-BR;q=0.8,pt;q=0.7',
        'cache-control': 'no-cache',
        'origin': 'https://fundamentus.com.br',
        'pragma': 'no-cache',
        'referer': 'https://fundamentus.com.br/buscaavancada.php',
        'sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
    }
    data = {
        'pl_min': '',
        'pl_max': '',
        'pvp_min': '',
        'pvp_max': '',
        'psr_min': '',
        'psr_max': '',
        'divy_min': '',
        'divy_max': '',
        'pativos_min': '',
        'pativos_max': '',
        'pcapgiro_min': '',
        'pcapgiro_max': '',
        'pebit_min': '',
        'pebit_max': '',
        'fgrah_min': '',
        'fgrah_max': '',
        'firma_ebit_min': '',
        'firma_ebit_max': '',
        'firma_ebitda_min': '',
        'firma_ebitda_max': '',
        'margemebit_min': '',
        'margemebit_max': '',
        'margemliq_min': '',
        'margemliq_max': '',
        'liqcorr_min': '',
        'liqcorr_max': '',
        'roic_min': '',
        'roic_max': '',
        'roe_min': '',
        'roe_max': '',
        'liq_min': '',
        'liq_max': '',
        'patrim_min': '',
        'patrim_max': '',
        'divbruta_min': '',
        'divbruta_max': '',
        'tx_cresc_rec_min': '',
        'tx_cresc_rec_max': '',
        'setor': '',
        'negociada': 'ON',
        'ordem': '1',
        'x': '38',
        'y': '9',
    }

    response = requests.post('https://fundamentus.com.br/resultado.php', headers=headers, data=data)

    selector = Selector(text=response.text)

    linhas_acoes = selector.css('tbody > tr')

    acoes = []
    for linha in linhas_acoes:
        acoes.append(
            {
                "CODIGO": linha.css('a::text').get(),
                "COTACAO": linha.css('td:nth-child(2)::text').get(),
                "P/L": linha.css('td:nth-child(3)::text').get(),
                "P/VP": linha.css('td:nth-child(4)::text').get(),
                "PSR": linha.css('td:nth-child(5)::text').get(),
                "DIV.YIELD %": linha.css('td:nth-child(6)::text').get(),
                "P/ATIVO": linha.css('td:nth-child(7)::text').get(),
                "P/CAP.GIRO": linha.css('td:nth-child(8)::text').get(),
                "P/EBIT": linha.css('td:nth-child(9)::text').get(),
                "P/ATIV.CIRC.LIQ": linha.css('td:nth-child(10)::text').get(),
                "EV/EBIT": linha.css('td:nth-child(11)::text').get(),
                "EV/EBITIDA": linha.css('td:nth-child(12)::text').get(),
                "MRG EBIT %": linha.css('td:nth-child(13)::text').get(),
                "MRG LIQ %": linha.css('td:nth-child(14)::text').get(),
                "LIQ CORR": linha.css('td:nth-child(15)::text').get(),
                "ROIC %": linha.css('td:nth-child(16)::text').get(),
                "ROE %": linha.css('td:nth-child(17)::text').get(),
                "LIQ 2M": linha.css('td:nth-child(18)::text').get(),
                "PATRIM LIQ": linha.css('td:nth-child(19)::text').get(),
                "DIV BRUTA/PATRIM": linha.css('td:nth-child(20)::text').get(),
                "CRESC REC 5A %": linha.css('td:nth-child(21)::text').get(),
            }
        )
    return acoes


def get_fiis() -> list:
    headers = {
        'authority': 'fundamentus.com.br',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-language': 'en-US,en;q=0.9,pt-BR;q=0.8,pt;q=0.7',
        'cache-control': 'no-cache',
        'origin': 'https://fundamentus.com.br',
        'pragma': 'no-cache',
        'referer': 'https://fundamentus.com.br/fii_buscaavancada.php',
        'sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
    }

    data = {
        'ffo_y_min': '',
        'ffo_y_max': '',
        'divy_min': '',
        'divy_max': '',
        'pvp_min': '',
        'pvp_max': '',
        'mk_cap_min': '',
        'mk_cap_max': '',
        'qtd_imoveis_min': '',
        'qtd_imoveis_max': '',
        'preco_m2_min': '',
        'preco_m2_max': '',
        'aluguel_m2_min': '',
        'aluguel_m2_max': '',
        'cap_rate_min': '',
        'cap_rate_max': '',
        'vacancia_min': '',
        'vacancia_max': '',
        'segmento': '',
        'negociada': 'ON',
        'x': '49',
        'y': '18',
    }

    response = requests.post('https://fundamentus.com.br/fii_resultado.php', headers=headers, data=data)

    selector = Selector(text=response.text)

    linhas_fiis = selector.css('tbody > tr')

    fiis = []
    for linha in linhas_fiis:
        fiis.append(
            {
                "CODIGO": linha.css('a::text').get(),
                "SEGMENTO": linha.css('td:nth-child(2)::text').get(),
                "COTACAO": linha.css('td:nth-child(3)::text').get(),
                "FFO YIELD %": linha.css('td:nth-child(4)::text').get(),
                "DIV.YIELD %": linha.css('td:nth-child(5)::text').get(),
                "P/VP": linha.css('td:nth-child(6)::text').get(),
                "VALOR DE MERCADO": linha.css('td:nth-child(7)::text').get(),
                "LIQUIDEZ": linha.css('td:nth-child(8)::text').get(),
                "QTD DE IMOVEIS": linha.css('td:nth-child(9)::text').get(),
                "PRECO DO M2": linha.css('td:nth-child(10)::text').get(),
                "ALUGUEL POR M2": linha.css('td:nth-child(11)::text').get(),
                "CAP RATE %": linha.css('td:nth-child(12)::text').get(),
                "VACANCIA MEDIA %": linha.css('td:nth-child(13)::text').get(),
            }
        )
    return fiis



