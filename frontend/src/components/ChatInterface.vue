<template>
  <div class="chat-container">
    <div class="chat-history">
      <div v-for="(message, index) in chatHistory" :key="index" :class="'message ' + message.sender">
        <div class="message-content">{{ message.text }}</div>
      </div>
    </div>
    <div class="input-area">
      <input type="text" v-model="newMessage" @keyup.enter="sendMessage" placeholder="Type your message here...">
      <button @click="sendMessage">Send</button>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      newMessage: '',
      chatHistory: [] , // {sender: 'user' | 'bot', text: 'message content'}
    };
  },
  methods: {
    async sendMessage() {
      if (this.newMessage.trim() === '') return;

      // 添加用户消息到聊天历史
      this.chatHistory.push({ sender: 'user', text: this.newMessage });

      try {
        const response = await axios.post('http://localhost:5000/api/chat/completions', {
          message: this.newMessage,
        });

        // 添加 DeepSeek 响应到聊天历史
        this.chatHistory.push({ sender: 'bot', text: response.data.response });
      } catch (error) {
        console.error('Error sending message:', error);
        this.chatHistory.push({ sender: 'bot', text: 'Error: Could not get response.' });
      }

      this.newMessage = ''; // 清空输入框
    },
  },
};
</script>

<style scoped>
.chat-container {
  width: 80%;
  max-width: 600px;
  margin: 0 auto;
  border: 1px solid #ccc;
  border-radius: 5px;
  padding: 10px;
}

.chat-history {
  height: 300px;
  overflow-y: scroll;
  margin-bottom: 10px;
}

.message {
  padding: 8px;
  border-radius: 5px;
  margin-bottom: 5px;
  word-wrap: break-word;
}

.message.user {
  background-color: #DCF8C6;
  text-align: right;
}

.message.bot {
  background-color: #ECE5DD;
  text-align: left;
}

.input-area {
  display: flex;
}

.input-area input {
  flex-grow: 1;
  padding: 8px;
  border: 1px solid #ccc;
  border-radius: 5px;
  margin-right: 5px;
}

.input-area button {
  padding: 8px 15px;
  background-color: #4CAF50;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}
</style>