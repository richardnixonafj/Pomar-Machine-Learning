from sklearn import tree

frutas = {"pera": 1, "laranja":2, "amora":3, "morango":4, "kiwi":5}
cores = {"amarelo": 1, "roxa": 2, "verde": 3, "vermelho": 4, "marrom": 5}


PesodaFruta = [
                [cores["verde"],100], [cores["verde"], 110], [cores["verde"],118],
                [cores["amarelo"], 130], [cores["amarelo"], 150], [cores["roxa"], 20],
                [cores["roxa"],30], [cores["roxa"], 24], [cores["roxa"], 32], [cores["vermelho"],50],
                [cores["vermelho"],60], [cores["vermelho"],70], [cores["marrom"],80], [cores["marrom"],85],
                [cores["marrom"],90]
                ]


resultado = [
            frutas["pera"], frutas["pera"],frutas["pera"], frutas["laranja"],
            frutas["laranja"], frutas["amora"], frutas["amora"],
            frutas["amora"], frutas["amora"], frutas["morango"], frutas["morango"],
            frutas["morango"], frutas["kiwi"] , frutas["kiwi"] , frutas["kiwi"]
             ]

clf = tree.DecisionTreeClassifier();
clf = clf.fit(PesodaFruta, resultado);

peso = input("Digite o peso da Fruta em miligramas: ");
corInput = input("Digite a cor da Fruta: ");

showResultado = clf.predict([[cores[corInput], peso]]);

print([k for k,v in frutas.items() if v == showResultado])