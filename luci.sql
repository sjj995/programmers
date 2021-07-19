// 루시와 엘라 찾기

SELECT ANIMAL_ID, NAME, SEX_UPON_INTAKE
FROM ANIMAL_INS
WHERE SEX_UPON_INTAKE = 'Spayed Female'
AND NAME IN ('Lucy', 'Ella','Pickle','Rogan', 'Sabrina', 'Mitty')
ORDER BY 1 ASC;