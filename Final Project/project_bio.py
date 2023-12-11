from sklearn.cross_decomposition import PLSRegression
from sklearn.model_selection import train_test_split,cross_val_score, cross_val_predict
from sklearn.linear_model import LogisticRegression
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis, QuadraticDiscriminantAnalysis
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
from sklearn.decomposition import PCA
import pandas as pd
from sklearn.metrics import confusion_matrix, classification_report
import matplotlib.pyplot as plt
import seaborn as sns

raw_counts = pd.read_csv(r'D:\Personal\Academics\UTA\3rd semester\Bioinformatics\Project\normalized_counts_vst.csv', index_col=0)
raw_counts = raw_counts.T
metadata_file = r"D:\Personal\Academics\UTA\3rd semester\Bioinformatics\Project\metadata.csv" 
metadata = pd.read_csv(metadata_file, sep=',')
df = pd.merge(raw_counts, metadata, left_index=True, right_on='Sample_ID')
df = df.drop(['Sample_ID','Clade', 'Dominant' ],axis=1)
df['Host'] = (df['Host']=='OANN').astype(int)
y = df['Host']
X = df.drop(['Host'],axis=1)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2,stratify=y, random_state=4)



pls = PLSRegression(n_components=10) 
y_pred_cv = cross_val_predict(pls, X_train, y_train, cv=5)
threshold = 0.5 
y_pred_cv = (y_pred_cv > threshold).astype(int)
cv_accuracy = accuracy_score(y_train, y_pred_cv)
print("Partial Least Square Cross-validated Accuracy:", cv_accuracy)
pls.fit(X_train, y_train)
y_pred = pls.predict(X_test)
threshold = 0.5
y_pred_binary = (y_pred > threshold).astype(int)
test_accuracy = accuracy_score(y_test, y_pred_binary)
print("Partial Least Square Test Set Accuracy:", test_accuracy)
conf_matrix = confusion_matrix(y_test, y_pred_binary)
plt.figure(figsize=(8, 6))
sns.heatmap(conf_matrix, annot=True, fmt="d", cmap="Blues", cbar=False)
plt.xlabel('Predicted')
plt.ylabel('True')
plt.title('Confusion Matrix for PLS')
plt.show()
print("Classification Report:")
print(classification_report(y_test, y_pred_binary))


lr = LogisticRegression(max_iter=1000)
cv_scores = cross_val_score(lr, X_train, y_train, cv=5, scoring='accuracy')
print("Logistic Regression Cross-validated Accuracy:", cv_scores.mean())
lr.fit(X_train, y_train)
y_pred = lr.predict(X_test)
test_accuracy = accuracy_score(y_test, y_pred)
print("Logistic Regression Test Set Accuracy:", test_accuracy)


svm = SVC()
cv_scores = cross_val_score(svm, X_train, y_train, cv=5, scoring='accuracy')
print("Support Vector Machine Cross-validated Accuracy:", cv_scores.mean())
svm.fit(X_train, y_train)
y_pred = svm.predict(X_test)
test_accuracy = accuracy_score(y_test, y_pred)
print("Support Vector Machine Test Set Accuracy:", test_accuracy)


lda = LinearDiscriminantAnalysis()
cv_scores = cross_val_score(lda, X_train, y_train, cv=5, scoring='accuracy')
print("Linear Discrimiant Analysis Cross-validated Accuracy:", cv_scores.mean())
lda.fit(X_train, y_train)
y_pred = lda.predict(X_test)
test_accuracy = accuracy_score(y_test, y_pred)
print("Linear Discrimiant Analysis Test Set Accuracy:", test_accuracy)


qda = QuadraticDiscriminantAnalysis()
n_components = min(X_train.shape[0], X_train.shape[1]) 
pca = PCA(n_components=10)  # Adjust the number of components as needed
X_train_pca = pca.fit_transform(X_train)
X_test_pca = pca.transform(X_test)
cv_scores = cross_val_score(qda, X_train_pca, y_train, cv=5, scoring='accuracy')
print("Quadratic Discrimiant Analysis Cross-validated Accuracy:", cv_scores.mean())
qda.fit(X_train_pca, y_train)
y_pred = qda.predict(X_test_pca)
test_accuracy = accuracy_score(y_test, y_pred)
print("Quadratic Discrimiant Analysis Test Set Accuracy:", test_accuracy)