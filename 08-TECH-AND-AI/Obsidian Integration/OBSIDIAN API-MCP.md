$headers = @{ Authorization = "Bearer f0f9e18765f4b482d22fe585f826a6cf2809b40c51a746c34c740e78c6ab3b7e" }

Invoke-RestMethod -Uri "http://127.0.0.1:27123/" -Headers $headers