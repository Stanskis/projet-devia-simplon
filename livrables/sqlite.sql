-- c3 est le prix unitaire
-- c4 est la quantité vendue

SELECT SUM(c3 * c4) AS CA FROM ventes;
-- Le chiffre d'affaires total est : 44825

SELECT c2 AS Produit, SUM(c4) AS Qte_vendue_par_produit FROM ventes WHERE c2 != 'produit' GROUP BY c2;
-- La quantité vendue par produit est :
-- Produit A: 1750
-- Produit B: 1055
-- Produit C: 575

SELECT c5 AS Region, SUM(c4) AS Qte_vendue_par_region FROM ventes WHERE c5 != 'region' GROUP BY c5;
-- La quantité vendue par région est :
-- Nord: 1605
-- Sud: 1775