"""
1. Define data, model, optimizer, loss_func, scheduler
2. Training/eval loop:
    1. train_losses, eval_losses = [], []
    1. for epoch in epochs:
        1. Train:
            1. total_train_loss, total_train_samples = 0, 0
            2. model.train()
            3. For train_batch in train_dataloader:
                1. Forward pass:
                    1. x, y = train_batch
                    2. x, y = x.to(device), y.to(device)
                    3. optimizer.zero_grad()
                    4. model_outputs = model(x)
                2. Backward pass:
                    1. loss = loss_func(model_outputs, y)
                    2. loss.backward()
                    3. optimizer.step()
                    4. bs = x.size(0)
                    5. total_train_loss += loss.item() * bs
                    5. total_train_samples += bs
            3. train_loss = total_train_loss / max(1, total_train_samples)
            4. train_losses.append(train_loss)
            5. scheduler.step()
        2. Eval (if epoch % eval_epochs == 0):
            1. total_eval_loss, total_eval_samples = 0, 0
            2. model.eval()
            3. with torch.no_grad():
                1. For eval_batch in train_dataloader:
                    1. x, y = eval_batch
                    2. x, y = x.to(device), y.to(device)
                    3. model_outputs = model(x)
                    4. loss = loss_func(model_outputs, y)
                    5. bs = x.size(0)
                    5. total_eval_loss += loss.item() * bs
                    6. total_eval_samples += bs
            4. eval_loss = total_eval_loss / max(1, total_eval_samples)
            5. eval_losses.append(eval_loss)
"""

import random

import torch
import torch.nn as nn
from torch.utils.data import DataLoader, Dataset


DEVICE = "cuda" if torch.cuda.is_available() else "cpu"
TRAIN_SAMPLES = 100
TEST_SAMPLES = 10
BATCH_SIZE = 32
NUM_CLASSES = 5
LR = 1e-3
SCHEDULER_STEP_SIZE = 10
SCHEDULER_GAMMA = 0.1
NUM_EPOCHS = 100
EVAL_EPOCHS = 5

# ---------- DATA ----------


def getRandom():
    dists = [
        lambda: random.gauss(0, 1),
        lambda: random.uniform(0, 1),
        lambda: random.expovariate(1),
        lambda: random.triangular(0, 1),
        lambda: random.lognormvariate(0, 1),
    ]
    i = random.randrange(len(dists))
    return dists[i](), i


class SampleDataset(Dataset):
    def __init__(self, n_samples: int) -> None:
        self.x = torch.empty(n_samples, 1, dtype=torch.float32)
        self.y = torch.empty(n_samples, dtype=torch.long)
        for idx in range(n_samples):
            val, cls = getRandom()
            self.x[idx, 0] = float(val)
            self.y[idx] = int(cls)

    def __len__(self) -> int:
        return self.x.size(0)

    def __getitem__(self, index: int):
        return self.x[index], self.y[index]


train_dataset = SampleDataset(TRAIN_SAMPLES)
test_dataset = SampleDataset(TEST_SAMPLES)

train_loader = DataLoader(train_dataset, batch_size=BATCH_SIZE, shuffle=True)
test_loader = DataLoader(test_dataset, batch_size=BATCH_SIZE, shuffle=False)


# ---------- MODEL ----------


class MLP(nn.Module):
    def __init__(self, in_dim: int = 1, num_classes: int = NUM_CLASSES) -> None:
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(in_dim, 32),
            nn.LeakyReLU(),
            nn.Dropout(p=0.1),
            nn.Linear(32, 32),
            nn.LeakyReLU(),
            nn.Dropout(p=0.1),
            nn.Linear(32, num_classes),
        )

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        return self.net(x)


model = MLP(in_dim=1, num_classes=NUM_CLASSES).to(DEVICE)

# ---------- LOSS ----------

loss_func = nn.CrossEntropyLoss()

# ---------- OPTIMIZER, SCHEDULER ----------

optimizer = torch.optim.AdamW(params=model.parameters(), lr=LR)
scheduler = torch.optim.lr_scheduler.StepLR(optimizer, step_size=SCHEDULER_STEP_SIZE, gamma=SCHEDULER_GAMMA)

# ---------- TRAINING, EVAL LOOP ----------

train_losses, eval_losses = [], []
for epoch in range(NUM_EPOCHS):
    model.train()
    total_train_loss = 0.0
    total_train_samples = 0

    for x, y in train_loader:
        x, y = x.to(DEVICE), y.to(DEVICE)

        optimizer.zero_grad(set_to_none=True)
        logits = model(x)
        loss = loss_func(logits, y)
        loss.backward()
        optimizer.step()

        bs = x.size(0)
        total_train_loss += loss.item() * bs
        total_train_samples += bs

    train_loss = total_train_loss / max(1, total_train_samples)
    train_losses.append(train_loss)

    scheduler.step()

    if epoch % EVAL_EPOCHS == 0:
        model.eval()
        total_eval_loss = 0.0
        total_eval_samples = 0

        with torch.no_grad():
            for x, y in test_loader:
                x, y = x.to(DEVICE), y.to(DEVICE)
                logits = model(x)
                loss = loss_func(logits, y)

                bs = x.size(0)
                total_eval_loss += loss.item() * bs
                total_eval_samples += bs

        eval_loss = total_eval_loss / max(1, total_eval_samples)
        eval_losses.append(eval_loss)
