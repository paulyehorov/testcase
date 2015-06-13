# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure(2) do |config|
    config.vm.box = "ubuntu/trusty64"
    config.ssh.insert_key = false

    config.vm.provider :virtualbox do |v|
        v.name = "testcase_flask"
        v.memory = 1024
        v.cpus = 2
    end

    config.vm.hostname = "testcase_flask"
    config.vm.network :private_network, ip: "192.168.0.100"

    config.vm.define :testcase_flask do |testcase_flask|
    end

    config.vm.provision "ansible" do |ansible|
        ansible.playbook = "provisioning/playbook.yml"
        ansible.inventory_path = "provisioning/inventory"
        ansible.sudo = true
    end

end
