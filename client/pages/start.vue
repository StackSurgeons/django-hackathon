<!-- <template>
  <v-container>
    <v-card class="card">
      <v-card-title>
        <h2>Hackathon Name</h2>
      </v-card-title>
      <v-card-text>
        <v-text-field v-model="hackathonName" label="Hackathon Name" outlined />
      </v-card-text>
    </v-card>

    <v-card
      class="card description"
      :style="{ height: hackathonDescriptionHeight }"
    >
      <v-card-title>
        <h3>Description</h3>
      </v-card-title>
      <v-card-text>
        <v-textarea outlined
          v-model="hackathonDescription"
          rows="5"
          ref="textarea"
          @input="adjustTextareaHeight"
        />
      </v-card-text>
    </v-card>

    <v-card class="card">
      <v-card-title>
        <h3>Dates</h3>
      </v-card-title>
      <v-card-text>
        <v-row>
          <v-col cols="6">
            <v-date-picker v-model="startDate" label="Start Date" />
          </v-col>
          <v-col cols="6">
            <v-date-picker v-model="endDate" label="End Date" />
          </v-col>
        </v-row>
      </v-card-text>
    </v-card>

    

    <v-card class="card">
      <v-card-title>
        <h3>Problem Statement</h3>
      </v-card-title>
      <v-card-text>
        <v-textarea v-model="problemStatement" rows="5" />
      </v-card-text>
    </v-card>

    <v-card class="card">
      <v-card-title>
        <h3>Rewards</h3>
      </v-card-title>
      <v-card-text>
        <v-row align="center">
          <v-col cols="6">
            <v-icon large @click="adjustRewards('up')">mdi-arrow-up</v-icon>
          </v-col>
          <v-col cols="6">
            <p>{{ reward }}</p>
          </v-col>
          <v-col cols="6">
            <v-icon large @click="adjustRewards('down')">mdi-arrow-down</v-icon>
          </v-col>
        </v-row>
      </v-card-text>
    </v-card>
    <v-card class="card">
      <v-card-title>
        <h3>Make Contest</h3>
      </v-card-title>
      <v-card-actions>
        <v-btn color="primary">Private</v-btn>
        <v-btn color="primary">Public</v-btn>
      </v-card-actions>
    </v-card>
    <v-card class="card">
      <v-card-title>
        <h3>External Links</h3>
      </v-card-title>
      <v-card-text>
        <v-row>
          <v-col cols="6">
            <v-card>
              <v-card-text>
                <h4>Link 1</h4>
                <p>Description 1</p>
              </v-card-text>
            </v-card>
          </v-col>
          <v-col cols="6">
            <v-card>
              <v-card-text>
                <h4>Link 2</h4>
                <p>Description 2</p>
              </v-card-text>
            </v-card>
          </v-col>
        </v-row>
      </v-card-text>
    </v-card>

    <v-card class="card">
      <v-card-actions>
        <v-btn color="primary" @click="startHackathon">Start</v-btn>
      </v-card-actions>
    </v-card>
  </v-container>
</template>


<style>
.container {
  display: flex;
  flex-wrap: wrap;
  gap: 20px;
}
.card {
  /* width: 45%; */
  padding: 20px;
  border: 1px solid #ccc;
  border-radius: 5px;
  box-sizing: border-box;
}
.card.description {
  flex-grow: 1;
}
</style> -->

