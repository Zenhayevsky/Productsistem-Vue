<template>
  <div class="container mt-2">
    <b-card
      style="background-color: #f0efea; color: #186a91"
      title="Nome do cliente"
    >
      <flex>
        <div>
          <b-card-text>
            <div>
              <div>
                <label>Status: </label>
                <input
                  type="text"
                  value="status do cliente"
                  style="border: none; background-color: transparent"
                />
              </div>
              <div>
                <label> Produto: </label>
                <input
                  type="text"
                  value="Produto do cliente"
                  style="border: none; background-color: transparent"
                />
              </div>
            </div>
          </b-card-text>
        </div>
        <b-button variant="outline-secondary" style="margin-right: 4px">
          Editar
        </b-button>
        <b-button variant="outline-primary">Excluir</b-button>
      </flex>
    </b-card>
  </div>
</template>
