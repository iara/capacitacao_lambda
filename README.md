Foram criados os seguintes serviços para o treinamento em lambda:

1. s3-xxx-dev-ue1-dl-origem-iara
2. lbd-xxx-dev-ue1-dl-minhaxxx-iara-1
3. sns-xxx-dev-ue1-dl-iara
4. sqs-xxx-dev-ue1-dl-minhaxxx-dll-iara
5. lbd-xxx-dev-ue1-dl-minhaxxx-iara-tolanding
5. s3-xxx-dev-ue1-dl-landing-iara
6. lbd-xxx-dev-ue1-dl-minhaxxx-iara-to-raw
7. s3-xxx-dev-ue1-dl-raw-iara OK
8. sqs-xxx-dev-ue1-dl-minhaxxx-dls-iara

O fluxo do criação dos serviços segue a seguinte ordem:

s3 -> lambda -> sns -> sqs -> lambda -> s3 -> lambda -> s3 -> sqs -> [BI]

Para baixar os pacotes python e subir no s3, ultilizar esse comando. 

- pip3 install -r requirement.txt --target .

Note que, se o zip com o código lambda e pacotes superarem 50 MB, a alternativa  a esse problema é usar as Layers do AWS Lambda.
