import torch
indice = torch.tensor([[0],
                      [1],
                      [2],
                       [3], 
                       [4]])
coord_y = indice.repeat((1, 5)) 
print(coord_y)
coord_y = coord_y.view((5 * 5,))
print(coord_y)
