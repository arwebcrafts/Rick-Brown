(function () {
  const navToggle = document.querySelector(".nav-toggle");
  const nav = document.querySelector(".nav");

  if (navToggle && nav) {
    navToggle.addEventListener("click", function () {
      const open = nav.classList.toggle("open");
      navToggle.setAttribute("aria-expanded", open ? "true" : "false");
    });

    nav.querySelectorAll("a").forEach(function (link) {
      link.addEventListener("click", function () {
        nav.classList.remove("open");
        navToggle.setAttribute("aria-expanded", "false");
      });
    });
  }

  // Preselect area from query string / hash
  const areaSelect = document.querySelector("#area");
  if (areaSelect) {
    const params = new URLSearchParams(window.location.search);
    const fromQuery = params.get("area");
    const fromHash = window.location.hash.replace("#", "");
    const area = fromQuery || (fromHash.startsWith("zip-") ? fromHash.replace("zip-", "") : "");
    if (area) {
      const option = Array.from(areaSelect.options).find(function (opt) {
        return opt.value === area || opt.textContent.toLowerCase().includes(area.toLowerCase());
      });
      if (option) areaSelect.value = option.value;
    }
  }

  const form = document.querySelector("#lead-form");
  if (!form) return;

  const status = document.querySelector("#form-status");

  form.addEventListener("submit", function (event) {
    event.preventDefault();

    const data = new FormData(form);
    const name = String(data.get("name") || "").trim();
    const phone = String(data.get("phone") || "").trim();
    const email = String(data.get("email") || "").trim();
    const area = String(data.get("area") || "").trim();
    const goal = String(data.get("goal") || "").trim();
    const message = String(data.get("message") || "").trim();

    if (!name || !phone || !email) {
      showStatus("Please fill in your name, phone, and email so Rick can reach you.", "err");
      return;
    }

    if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)) {
      showStatus("Please enter a valid email address.", "err");
      return;
    }

    const subject = encodeURIComponent(
      "Real Estate Inquiry from " + name + (area ? " (" + area + ")" : "")
    );

    const body = encodeURIComponent(
      [
        "New lead from rickbrownhomes.com landing page",
        "",
        "Name: " + name,
        "Phone: " + phone,
        "Email: " + email,
        "Area / ZIP: " + (area || "Not specified"),
        "Goal: " + (goal || "Not specified"),
        "",
        "Message:",
        message || "(none)",
        "",
        "Submitted: " + new Date().toLocaleString()
      ].join("\n")
    );

    // Functional fallback: opens the agent email with a ready lead draft
    window.location.href =
      "mailto:rick.brown@remax.net?subject=" + subject + "&body=" + body;

    showStatus(
      "Thanks, " + name.split(" ")[0] + ". Your email draft is opening so you can send it to Rick. You can also call or text 847-400-6018.",
      "ok"
    );

    form.reset();
  });

  function showStatus(text, type) {
    if (!status) return;
    status.textContent = text;
    status.className = "form-status " + type;
  }
})();
