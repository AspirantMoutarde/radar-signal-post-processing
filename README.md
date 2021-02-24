# radar-signal-post-processing
Post processing of a radar signal (school project)

- Esseyez de ne pas écrire de foncion ou de plot dans le main.
  Il ne doit contenir que des appels de fonctions (y compris pour les plots).
  Cela le rendra clair et facilement lisible.
  
  Déroulement de la chaine de post traitement (Main)


→ In : txt file (two columns of integers), Fsamp, Trec



Priority 1 : 
- Se, Sr = load(txt)
- MatrixSe = formatMAtrix(Se)
- MatrixSr = formatMAtrix(Sr)
- MatrixSi = correlateMatrix(MatrixSe, MatrixSr)
- MatrixCibles = CFARMatrix(MatrixSi)
- MatrixDistances = DistancesMatrix(MatrixCibles)
- trackingMatrix = k-NN(MatrixDistances)

Priority 2 : 
- units test
- Addition of signal and radar tests to classify its unit test capabilities.
- Plot for every steps


Priority 3 : 
- IHM JAVA (export od the py project as API ?)
- Treatment backup tool
