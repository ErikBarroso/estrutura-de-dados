#include <iostream>
using namespace std;

struct Node{
  int data;
  Node *left;
  Node *right;
  Node(int value) : data(value), left(nullptr), right(nullptr) {}
};

Node* insert(Node* root, int value) {
  if(root == nullptr) {
    return new Node(value);
  }

  if( value > root ->data) {
    root->right = insert(root ->right, value);
  } else {
    root-> left = insert(root->left, value);
  }

  return root;
}

//imprime o nó raiz, dps o filho esquerdo, dps o direito.
void preorderTraversal(Node *root) {
  if (root == nullptr) {
    return;
  }
  cout << root->data << endl;
  preorderTraversal(root->left);
  preorderTraversal(root->right);
}

/*
                                  10
                    2                           20       
               0      5                14    
                         10
*/

// vai para esquerda, direita e imprimi o no quando n tem mais nada.
void postorderTraversal(Node *root){
  if (root == nullptr){
    return;
  }
  postorderTraversal(root->left);
  postorderTraversal(root->right);
  cout << root->data << endl;
}

//imprimi em ordem crescente
void inorderTraversal(Node *root){
  if (root == nullptr){
    return;
  }
  inorderTraversal(root->left);
  cout << root->data << endl;
  inorderTraversal(root->right);
}

int main () {
  Node* binaryTree = insert(nullptr, 10);
  insert(binaryTree, 20);
  insert(binaryTree, 2);
  insert(binaryTree, 5);
  insert(binaryTree, 10);
  insert(binaryTree, 0);
  insert(binaryTree, 14);
  inorderTraversal(binaryTree);
  return 0;
}